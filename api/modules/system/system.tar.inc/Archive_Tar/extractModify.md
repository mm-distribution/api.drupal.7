# Archive_Tar::extractModify()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 627–646 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L627-L646)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function extractModify($p_path, $p_remove_path, $p_preserve = false, $p_symlinks = true)
```

## Documentation

```text
This method extract all the content of the archive in the directory
indicated by $p_path. When relevant the memorized path of the
files/dir can be modified by removing the $p_remove_path path at the
beginning of the file/dir path.
While extracting a file, if the directory path does not exists it is
created.
While extracting a file, if the file already exists it is replaced
without looking for last modification date.
While extracting a file, if the file already exists and is write
protected, the extraction is aborted.
While extracting a file, if a directory with the same name already
exists, the extraction is aborted.
While extracting a directory, if a file with the same name already
exists, the extraction is aborted.
While extracting a file/directory if the destination directory exist
and is write protected, or does not exist but can not be created,
the extraction is aborted.
If after extraction an extracted file does not show the correct
stored file size, the extraction is aborted.
When the extraction is aborted, a PEAR error text is set and false
is returned. However the result can be a partial extraction that may
need to be manually cleaned.

@param string $p_path The path of the directory where the
                              files/dir need to by extracted.
@param string $p_remove_path Part of the memorized path that can be
                              removed if present at the beginning of
                              the file/dir path.
@param boolean $p_preserve Preserve user/group ownership of files
@param boolean $p_symlinks Allow symlinks.

@return boolean true on success, false on error.
@see    extractList()
```

## Code

```php
    public function extractModify($p_path, $p_remove_path, $p_preserve = false, $p_symlinks = true)
    {
        $v_result = true;
        $v_list_detail = array();

        if ($v_result = $this->_openRead()) {
            $v_result = $this->_extractList(
                $p_path,
                $v_list_detail,
                "complete",
                0,
                $p_remove_path,
                $p_preserve,
                $p_symlinks
            );
            $this->_close();
        }

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
