# Archive_Tar::_addList()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1194–1270 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1194-L1270)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _addList($p_list, $p_add_dir, $p_remove_dir)
```

## Documentation

```text
@param array $p_list
@param string $p_add_dir
@param string $p_remove_dir
@return bool
```

## Code

```php
    public function _addList($p_list, $p_add_dir, $p_remove_dir)
    {
        $v_result = true;
        $v_header = array();

        // ----- Remove potential windows directory separator
        $p_add_dir = $this->_translateWinPath($p_add_dir);
        $p_remove_dir = $this->_translateWinPath($p_remove_dir, false);

        if (!$this->_file) {
            $this->_error('Invalid file descriptor');
            return false;
        }

        if (sizeof($p_list) == 0) {
            return true;
        }

        foreach ($p_list as $v_filename) {
            if (!$v_result) {
                break;
            }

            // ----- Skip the current tar name
            if ($v_filename == $this->_tarname) {
                continue;
            }

            if ($v_filename == '') {
                continue;
            }

            // ----- ignore files and directories matching the ignore regular expression
            if ($this->_ignore_regexp && preg_match($this->_ignore_regexp, '/' . $v_filename)) {
                $this->_warning("File '$v_filename' ignored");
                continue;
            }

            if (!file_exists($v_filename) && !is_link($v_filename)) {
                $this->_warning("File '$v_filename' does not exist");
                continue;
            }

            // ----- Add the file or directory header
            if (!$this->_addFile($v_filename, $v_header, $p_add_dir, $p_remove_dir)) {
                return false;
            }

            if (@is_dir($v_filename) && !@is_link($v_filename)) {
                if (!($p_hdir = opendir($v_filename))) {
                    $this->_warning("Directory '$v_filename' can not be read");
                    continue;
                }
                while (false !== ($p_hitem = readdir($p_hdir))) {
                    if (($p_hitem != '.') && ($p_hitem != '..')) {
                        if ($v_filename != ".") {
                            $p_temp_list[0] = $v_filename . '/' . $p_hitem;
                        } else {
                            $p_temp_list[0] = $p_hitem;
                        }

                        $v_result = $this->_addList(
                            $p_temp_list,
                            $p_add_dir,
                            $p_remove_dir
                        );
                    }
                }

                unset($p_temp_list);
                unset($p_hdir);
                unset($p_hitem);
            }
        }

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
