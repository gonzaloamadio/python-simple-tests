import zipfile
from zipfile import ZipFile, ZipInfo
from io import BytesIO
import pytest
import os


def _prepare_zip_content(content, input_extension, input_filename, processing_dir):
    input_full_filename = '.'.join([input_filename, input_extension])
    # As we fetch the content of the zip file, write it on a zip file so it is easier to manipulate.
    zip_filepath = os.path.join(processing_dir, input_full_filename)

    # Write streamed content to file
    with open(zip_filepath, 'wb') as file:
        file.write(content)

    # Extract zip content
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(processing_dir)

    os.remove(zip_filepath)


def create_zip_v2():
    """
    returns: zip archive
    """
    archive = BytesIO()

    with ZipFile(archive, 'w') as zip_archive:
        # Create three files on zip archive

        file1 = ZipInfo('session1.x1s')
        zip_archive.writestr(file1, b'compose-file-content...')

        file2 = ZipInfo('session2.x1s')
        zip_archive.writestr(file2, b'app-config-content...')

        file3 = ZipInfo('session3.x1s')
        zip_archive.writestr(file3, b'root-config-content...')

    return archive


def test_prepare_zip_content(tmpdir_factory):

    tmpfolder = tmpdir_factory.mktemp("tmpdir")
    tmpfolder = tmpfolder.strpath

    # This it is, or it may be, like pulling a zip file from an API
    archive = create_zip_v2()

    _prepare_zip_content(archive.getbuffer(), "zip", "sesions", tmpfolder)
    # Expected values
    names = ["session1.x1s", "session2.x1s", "session3.x1s"]
    actual_names = []
    for filename in os.listdir(tmpfolder):
        actual_names.append(filename)

    assert len(actual_names) == 3
    assert sorted(actual_names) == sorted(names)
