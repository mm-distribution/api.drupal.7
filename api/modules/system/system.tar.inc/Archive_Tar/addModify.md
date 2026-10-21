# Archive_Tar::addModify()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 509–533 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L509-L533)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function addModify($p_filelist, $p_add_dir, $p_remove_dir = '')
```

## Documentation

```text
This method add the files / directories listed in $p_filelist at the
end of the existing archive. If the archive does not yet exists it
is created.
The $p_filelist parameter can be an array of string, each string
representing a filename or a directory name with their path if
needed. It can also be a single string with names separated by a
single blank.
The path indicated in $p_remove_dir will be removed from the
memorized path of each file / directory listed when this path
exists. By default nothing is removed (empty path '')
The path indicated in $p_add_dir will be added at the beginning of
the memorized path of each file / directory listed. However it can
be set to empty ''. The adding of a path is done after the removing
of path.
The path add/remove ability enables the user to prepare an archive
for extraction in a different path than the origin files are.
If a file/dir is already in the archive it will only be added at the
end of the archive. There is no update of the existing archived
file/dir. However while extracting the archive, the last file will
replace the first one. This results in a none optimization of the
archive size.
If a file/dir does not exist the file/dir is ignored. However an
error text is send to PEAR error.
If a file/dir is not readable the file/dir is ignored. However an
error text is send to PEAR error.

@param array $p_filelist An array of filenames and directory
                            names, or a single string with names
                            separated by a single blank space.
@param string $p_add_dir A string which contains a path to be
                            added to the memorized path of each
                            element in the list.
@param string $p_remove_dir A string which contains a path to be
                            removed from the memorized path of
                            each element in the list, when
                            relevant.

@return bool true on success, false on error.
```

## Code

```php
    public function addModify($p_filelist, $p_add_dir, $p_remove_dir = '')
    {
        $v_result = true;

        if (!$this->_isArchive()) {
            $v_result = $this->createModify(
                $p_filelist,
                $p_add_dir,
                $p_remove_dir
            );
        } else {
            if (is_array($p_filelist)) {
                $v_list = $p_filelist;
            } elseif (is_string($p_filelist)) {
                $v_list = explode($this->_separator, $p_filelist);
            } else {
                $this->_error('Invalid file list');
                return false;
            }

            $v_result = $this->_append($v_list, $p_add_dir, $p_remove_dir);
        }

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
