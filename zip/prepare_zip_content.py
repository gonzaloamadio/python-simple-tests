import os, shutil
import pytest
import zipfile


def delete_file_or_folder(file_path):
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def prepare_zip_content(zip_filepath, processing_dir):

    # As we fetch the content of the zip file, write it on a zip file so it is easier to manipulate.
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(processing_dir)

    delete_file_or_folder(zip_filepath)
    zip_filepath = os.path.join(processing_dir, "sessions.zip")
    delete_file_or_folder(zip_filepath)

    for filename in os.listdir(processing_dir):
        if filename == '.keep':
            continue
        filepath = os.path.join(processing_dir, filename)
        if not filename.endswith('.bri'):
            delete_file_or_folder(filepath)
        else:
            # Delete bri extension. From .x1s.bri to .x1s
            x1s_filepath = filepath.rsplit('.', 1)[0]
            os.rename(filepath, x1s_filepath)

def test_prepare_zip_content(tmpdir_factory):

    # Create folders
    tmpfolder = tmpdir_factory.mktemp("tmpdir")
    tmpfolder = tmpfolder.strpath
    proc_folder = tmpdir_factory.mktemp("processing")
    processing_dir = proc_folder.strpath
    zip_filepath = os.path.join(tmpfolder, "sessions")

    # Create 3 files
    for i in range(3):
        tempfile = os.path.join(tmpfolder, f"file_{i}.x1s.bri")
        with open(tempfile, "w") as brifile:
            brifile.write("asd")

    # zip folder with files
    shutil.make_archive(zip_filepath,"zip", tmpfolder)

    # Execute function
    zip_filepath = os.path.join(tmpfolder, "sessions.zip")
    prepare_zip_content(zip_filepath, processing_dir)

    # Expected values
    names = ["file_0.x1s", "file_1.x1s", "file_2.x1s"]
    actual_names = []
    for filename in os.listdir(processing_dir):
        actual_names.append(filename)

    assert len(actual_names) == 3
    assert sorted(actual_names) == sorted(names)
