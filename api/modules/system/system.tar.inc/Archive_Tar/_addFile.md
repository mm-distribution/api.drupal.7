# Archive_Tar::_addFile()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1280–1357 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1280-L1357)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _addFile($p_filename, &$p_header, $p_add_dir, $p_remove_dir, $v_stored_filename = null)
```

## Documentation

```text
@param string $p_filename
@param mixed $p_header
@param string $p_add_dir
@param string $p_remove_dir
@param null $v_stored_filename
@return bool
```

## Code

```php
    public function _addFile($p_filename, &$p_header, $p_add_dir, $p_remove_dir, $v_stored_filename = null)
    {
        if (!$this->_file) {
            $this->_error('Invalid file descriptor');
            return false;
        }

        if ($p_filename == '') {
            $this->_error('Invalid file name');
            return false;
        }

        if (is_null($v_stored_filename)) {
            // ----- Calculate the stored filename
            $p_filename = $this->_translateWinPath($p_filename, false);
            $v_stored_filename = $p_filename;

            if (strcmp($p_filename, $p_remove_dir) == 0) {
                return true;
            }

            if ($p_remove_dir != '') {
                if (substr($p_remove_dir, -1) != '/') {
                    $p_remove_dir .= '/';
                }

                if (substr($p_filename, 0, strlen($p_remove_dir)) == $p_remove_dir) {
                    $v_stored_filename = substr($p_filename, strlen($p_remove_dir));
                }
            }

            $v_stored_filename = $this->_translateWinPath($v_stored_filename);
            if ($p_add_dir != '') {
                if (substr($p_add_dir, -1) == '/') {
                    $v_stored_filename = $p_add_dir . $v_stored_filename;
                } else {
                    $v_stored_filename = $p_add_dir . '/' . $v_stored_filename;
                }
            }

            $v_stored_filename = $this->_pathReduction($v_stored_filename);
        }

        if ($this->_isArchive($p_filename)) {
            if (($v_file = @fopen($p_filename, "rb")) == 0) {
                $this->_warning(
                    "Unable to open file '" . $p_filename
                    . "' in binary read mode"
                );
                return true;
            }

            if (!$this->_writeHeader($p_filename, $v_stored_filename)) {
                return false;
            }

            while (($v_buffer = fread($v_file, $this->buffer_length)) != '') {
                $buffer_length = strlen("$v_buffer");
                if ($buffer_length != $this->buffer_length) {
                    $pack_size = ((int)($buffer_length / 512) + ($buffer_length % 512 !== 0 ? 1 : 0)) * 512;
                    $pack_format = sprintf('a%d', $pack_size);
                } else {
                    $pack_format = sprintf('a%d', $this->buffer_length);
                }
                $v_binary_data = pack($pack_format, "$v_buffer");
                $this->_writeBlock($v_binary_data);
            }

            fclose($v_file);
        } else {
            // ----- Only header for dir
            if (!$this->_writeHeader($p_filename, $v_stored_filename)) {
                return false;
            }
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
