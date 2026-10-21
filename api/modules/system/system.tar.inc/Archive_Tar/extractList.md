# Archive_Tar::extractList()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 689–717 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L689-L717)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function extractList($p_filelist, $p_path = '', $p_remove_path = '', $p_preserve = false, $p_symlinks = true)
```

## Documentation

```text
This method extract from the archive only the files indicated in the
$p_filelist. These files are extracted in the current directory or
in the directory indicated by the optional $p_path parameter.
If indicated the $p_remove_path can be used in the same way as it is
used in extractModify() method.

@param array $p_filelist An array of filenames and directory names,
                              or a single string with names separated
                              by a single blank space.
@param string $p_path The path of the directory where the
                              files/dir need to by extracted.
@param string $p_remove_path Part of the memorized path that can be
                              removed if present at the beginning of
                              the file/dir path.
@param boolean $p_preserve Preserve user/group ownership of files
@param boolean $p_symlinks Allow symlinks.

@return bool true on success, false on error.
@see    extractModify()
```

## Code

```php
    public function extractList($p_filelist, $p_path = '', $p_remove_path = '', $p_preserve = false, $p_symlinks = true)
    {
        $v_result = true;
        $v_list_detail = array();

        if (is_array($p_filelist)) {
            $v_list = $p_filelist;
        } elseif (is_string($p_filelist)) {
            $v_list = explode($this->_separator, $p_filelist);
        } else {
            $this->_error('Invalid string list');
            return false;
        }

        if ($v_result = $this->_openRead()) {
            $v_result = $this->_extractList(
                $p_path,
                $v_list_detail,
                "partial",
                $v_list,
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
