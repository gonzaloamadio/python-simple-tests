import os, shutil
import pytest
import zipfile


def print_file_in_dir(path):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        print(full_path)


def empty_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        delete_file_or_folder(file_path)


def delete_file_or_folder(file_path):
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def print_log(text):
    print("---------------------------------------")
    print(text)
    print("---------------------------------------")


def prepare_zip_content(zip_filepath, processing_dir):

    # As we fetch the content of the zip file, write it on a zip file so it is easier to manipulate.
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(processing_dir)
    # This is the same as doing this : but we can filter filename with these
    # next lines if we would like to
    #    listOfFileNames = zipObj.namelist()
    #    for fileName in listOfFileNames:
    #        zipObj.extract(fileName, f"{processing_dir}/{fileName}")

    print_log("Before deleting the zip file thats inside the zip file")
    print(print_file_in_dir(processing_dir))

    for filename in os.listdir(processing_dir):
        if filename == '.keep':
            continue
        filepath = os.path.join(processing_dir, filename)
        # TODO: is this ok? Or raise exception?
        if not filename.endswith('.ext2'):
            delete_file_or_folder(filepath)
        else:
            # Delete last extension
            ext1_filepath = filepath.rsplit('.', 1)[0]
            os.rename(filepath, ext1_filepath)

    print_log("After renaming and deleting some files")
    print(print_file_in_dir(processing_dir))


def test_prepare_zip_content(tmpdir_factory):

    tmpfolder = tmpdir_factory.mktemp("tmpdir")
    tmpfolder = tmpfolder.strpath

    proc_folder = tmpdir_factory.mktemp("processing")
    processing_dir = proc_folder.strpath

    zip_filepath = os.path.join(tmpfolder, "sessions")

    # Create 3 files
    for i in range(3):
        tempfile = os.path.join(tmpfolder, f"file_{i}.ext1.ext2")
        with open(tempfile, "w") as brifile:
            brifile.write("asd")

    shutil.make_archive(zip_filepath,"zip", tmpfolder)

    #####################################################

    # Si agregamos asi, nos agrega con todo el path directo.
    # Entonces cuando hacemos el extract, tenemos algo asi:
    # ['tmp/pytest-of-gamadio/pytest-26/tmpdir0/file_0.ext1.ext2',
    #  'tmp/pytest-of-gamadio/pytest-26/tmpdir0/sessions.zip',
    #  'tmp/pytest-of-gamadio/pytest-26/tmpdir0/file_2.ext1.ext2',
    #  'tmp/pytest-of-gamadio/pytest-26/tmpdir0/file_1.ext1.ext2']

    # zip_filepath = os.path.join(tmpfolder, "sessions.zip")
#    with zipfile.ZipFile(zip_filepath,"a") as zfile:
#        for filename in os.listdir(tmpfolder):
#            zfile.write(tmpfolder+"/"+filename)

    # Solucionarlo con! : https://stackoverflow.com/questions/34270582/adding-file-to-existing-zipfile/34270963#34270963
    # Basically, add actual name as second argument of write.

    #zip_filepath = os.path.join(tmpfolder, "sessions.zip")
    #with zipfile.ZipFile(zip_filepath,"a") as zfile:
    #   for filename in os.listdir(tmpfolder):
    #       path = os.path.join(tmpfolder, filename)
    #       zfile.write(path, os.path.basename(path))

    #####################################################

    zip_filepath = os.path.join(tmpfolder, "sessions.zip")
    with zipfile.ZipFile(zip_filepath,"r") as zfile:
        print(zfile.namelist())

    prepare_zip_content(zip_filepath, processing_dir)

    names = ["file_0.ext1", "file_1.ext1", "file_2.ext1"]
    actual_names = []
    for filename in os.listdir(processing_dir):
        actual_names.append(filename)

    assert len(actual_names) == 3
    assert sorted(actual_names) == sorted(names)
