# Archive_Tar

- **Type:** Class
- **File:** [`modules/system/system.tar.inc`](_file.md), lines 102–2593 · [local source](../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L102-L2593)
- **Module/theme:** system

## Signature

```php
class Archive_Tar
```

## Documentation

```text
Creates a (compressed) Tar archive

@package Archive_Tar
@author  Vincent Blavet <vincent@phpconcept.net>
@license http://www.opensource.org/licenses/bsd-license.php New BSD License
@version $Revision$
```

## Properties

### $_tarname

```php
public $_tarname = '';
```

```text
@var string Name of the Tar
```

### $_compress

```php
public $_compress = false;
```

```text
@var boolean if true, the Tar file will be gzipped
```

### $_compress_type

```php
public $_compress_type = 'none';
```

```text
@var string Type of compression : 'none', 'gz', 'bz2' or 'lzma2'
```

### $_separator

```php
public $_separator = ' ';
```

```text
@var string Explode separator
```

### $_file

```php
public $_file = 0;
```

```text
@var file descriptor
```

### $_temp_tarname

```php
public $_temp_tarname = '';
```

```text
@var string Local Tar name of a remote Tar (http:// or ftp://)
```

### $_ignore_regexp

```php
public $_ignore_regexp = '';
```

```text
@var string regular expression for ignoring files or directories
```

### $error_object

```php
public $error_object = null;
```

```text
@var object PEAR_Error object
```

### $_fmt

```php
public $_fmt = '';
```

```text
Format for data extraction

@var string
```

### $buffer_length

```php
protected $buffer_length;
```

```text
@var int Length of the read buffer in bytes
```

## Methods (derived index)

- [__construct()](Archive_Tar/__construct.md) — Archive_Tar Class constructor. This flavour of the constructor only declare a new Archive_Tar object, identifying it by the name of the tar file. If the compress argument is set the tar will be read or created as a gzip or bz2 compressed TAR file.
- [__destruct()](Archive_Tar/__destruct.md)
- [loadExtension()](Archive_Tar/loadExtension.md) — OS independent PHP extension load. Remember to take care on the correct extension name for case sensitive OSes.
- [create()](Archive_Tar/create.md) — This method creates the archive file and add the files / directories that are listed in $p_filelist. If a file with the same name exist and is writable, it is replaced by the new tar. The method return false and a PEAR error text. The $p_filelist parameter can be an array of string, each string representing a filename or a directory name with their path if needed. It can also be a single string with names separated by a single blank. For each directory added in the archive, the files and sub-directories are also added. See also createModify() method for more details.
- [add()](Archive_Tar/add.md) — This method add the files / directories that are listed in $p_filelist in the archive. If the archive does not exist it is created. The method return false and a PEAR error text. The files and directories listed are only added at the end of the archive, even if a file with the same name is already archived. See also createModify() method for more details.
- [extract()](Archive_Tar/extract.md)
- [listContent()](Archive_Tar/listContent.md)
- [createModify()](Archive_Tar/createModify.md) — This method creates the archive file and add the files / directories that are listed in $p_filelist. If the file already exists and is writable, it is replaced by the new tar. It is a create and not an add. If the file exists and is read-only or is a directory it is not replaced. The method return false and a PEAR error text. The $p_filelist parameter can be an array of string, each string representing a filename or a directory name with their path if needed. It can also be a single string with names separated by a single blank. The path indicated in $p_remove_dir will be removed from the memorized path of each file / directory listed when this path exists. By default nothing is removed (empty path '') The path indicated in $p_add_dir will be added at the beginning of the memorized path of each file / directory listed. However it can be set to empty ''. The adding of a path is done after the removing of path. The path add/remove ability enables the user to prepare an archive for extraction in a different path than the origin files are. See also addModify() method for file adding properties.
- [addModify()](Archive_Tar/addModify.md) — This method add the files / directories listed in $p_filelist at the end of the existing archive. If the archive does not yet exists it is created. The $p_filelist parameter can be an array of string, each string representing a filename or a directory name with their path if needed. It can also be a single string with names separated by a single blank. The path indicated in $p_remove_dir will be removed from the memorized path of each file / directory listed when this path exists. By default nothing is removed (empty path '') The path indicated in $p_add_dir will be added at the beginning of the memorized path of each file / directory listed. However it can be set to empty ''. The adding of a path is done after the removing of path. The path add/remove ability enables the user to prepare an archive for extraction in a different path than the origin files are. If a file/dir is already in the archive it will only be added at the end of the archive. There is no update of the existing archived file/dir. However while extracting the archive, the last file will replace the first one. This results in a none optimization of the archive size. If a file/dir does not exist the file/dir is ignored. However an error text is send to PEAR error. If a file/dir is not readable the file/dir is ignored. However an error text is send to PEAR error.
- [addString()](Archive_Tar/addString.md) — This method add a single string as a file at the end of the existing archive. If the archive does not yet exists it is created.
- [extractModify()](Archive_Tar/extractModify.md) — This method extract all the content of the archive in the directory indicated by $p_path. When relevant the memorized path of the files/dir can be modified by removing the $p_remove_path path at the beginning of the file/dir path. While extracting a file, if the directory path does not exists it is created. While extracting a file, if the file already exists it is replaced without looking for last modification date. While extracting a file, if the file already exists and is write protected, the extraction is aborted. While extracting a file, if a directory with the same name already exists, the extraction is aborted. While extracting a directory, if a file with the same name already exists, the extraction is aborted. While extracting a file/directory if the destination directory exist and is write protected, or does not exist but can not be created, the extraction is aborted. If after extraction an extracted file does not show the correct stored file size, the extraction is aborted. When the extraction is aborted, a PEAR error text is set and false is returned. However the result can be a partial extraction that may need to be manually cleaned.
- [extractInString()](Archive_Tar/extractInString.md) — This method extract from the archive one file identified by $p_filename. The return value is a string with the file content, or NULL on error.
- [extractList()](Archive_Tar/extractList.md) — This method extract from the archive only the files indicated in the $p_filelist. These files are extracted in the current directory or in the directory indicated by the optional $p_path parameter. If indicated the $p_remove_path can be used in the same way as it is used in extractModify() method.
- [setAttribute()](Archive_Tar/setAttribute.md) — This method set specific attributes of the archive. It uses a variable list of parameters, in the format attribute code + attribute values : $arch->setAttribute(ARCHIVE_TAR_ATT_SEPARATOR, ',');
- [setIgnoreRegexp()](Archive_Tar/setIgnoreRegexp.md) — This method sets the regular expression for ignoring files and directories at import, for example: $arch->setIgnoreRegexp("#CVS|\.svn#");
- [setIgnoreList()](Archive_Tar/setIgnoreList.md) — This method sets the regular expression for ignoring all files and directories matching the filenames in the array list at import, for example: $arch->setIgnoreList(array('CVS', '.svn', 'bin/tool'));
- [_error()](Archive_Tar/_error.md)
- [_warning()](Archive_Tar/_warning.md)
- [_isArchive()](Archive_Tar/_isArchive.md)
- [_openWrite()](Archive_Tar/_openWrite.md)
- [_openRead()](Archive_Tar/_openRead.md)
- [_openReadWrite()](Archive_Tar/_openReadWrite.md)
- [_close()](Archive_Tar/_close.md)
- [_cleanFile()](Archive_Tar/_cleanFile.md)
- [_writeBlock()](Archive_Tar/_writeBlock.md)
- [_readBlock()](Archive_Tar/_readBlock.md)
- [_jumpBlock()](Archive_Tar/_jumpBlock.md)
- [_writeFooter()](Archive_Tar/_writeFooter.md)
- [_addList()](Archive_Tar/_addList.md)
- [_addFile()](Archive_Tar/_addFile.md)
- [_addString()](Archive_Tar/_addString.md)
- [_writeHeader()](Archive_Tar/_writeHeader.md)
- [_writeHeaderBlock()](Archive_Tar/_writeHeaderBlock.md)
- [_writeLongHeader()](Archive_Tar/_writeLongHeader.md)
- [_readHeader()](Archive_Tar/_readHeader.md)
- [_tarRecToSize()](Archive_Tar/_tarRecToSize.md) — Convert Tar record size to actual size
- [_isMaliciousFilename()](Archive_Tar/_isMaliciousFilename.md) — Detect and report a malicious file name
- [_readLongHeader()](Archive_Tar/_readLongHeader.md)
- [_extractInString()](Archive_Tar/_extractInString.md) — This method extract from the archive one file identified by $p_filename. The return value is a string with the file content, or null on error.
- [_extractList()](Archive_Tar/_extractList.md)
- [_openAppend()](Archive_Tar/_openAppend.md)
- [_append()](Archive_Tar/_append.md)
- [_dirCheck()](Archive_Tar/_dirCheck.md) — Check if a directory exists and create it (including parent dirs) if not.
- [_pathReduction()](Archive_Tar/_pathReduction.md) — Compress path by changing for example "/dir/foo/../bar" to "/dir/bar", rand emove double slashes.
- [_translateWinPath()](Archive_Tar/_translateWinPath.md)

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
