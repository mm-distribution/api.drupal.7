# Archive_Tar::createModify()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 437–467 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L437-L467)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function createModify($p_filelist, $p_add_dir, $p_remove_dir = '')
```

## Documentation

```text
This method creates the archive file and add the files / directories
that are listed in $p_filelist.
If the file already exists and is writable, it is replaced by the
new tar. It is a create and not an add. If the file exists and is
read-only or is a directory it is not replaced. The method return
false and a PEAR error text.
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
See also addModify() method for file adding properties.

@param array $p_filelist An array of filenames and directory names,
                            or a single string with names separated by
                            a single blank space.
@param string $p_add_dir A string which contains a path to be added
                            to the memorized path of each element in
                            the list.
@param string $p_remove_dir A string which contains a path to be
                            removed from the memorized path of each
                            element in the list, when relevant.

@return boolean true on success, false on error.
@see addModify()
```

## Code

```php
    public function createModify($p_filelist, $p_add_dir, $p_remove_dir = '')
    {
        $v_result = true;

        if (!$this->_openWrite()) {
            return false;
        }

        if ($p_filelist != '') {
            if (is_array($p_filelist)) {
                $v_list = $p_filelist;
            } elseif (is_string($p_filelist)) {
                $v_list = explode($this->_separator, $p_filelist);
            } else {
                $this->_cleanFile();
                $this->_error('Invalid file list');
                return false;
            }

            $v_result = $this->_addList($v_list, $p_add_dir, $p_remove_dir);
        }

        if ($v_result) {
            $this->_writeFooter();
            $this->_close();
        } else {
            $this->_cleanFile();
        }

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
