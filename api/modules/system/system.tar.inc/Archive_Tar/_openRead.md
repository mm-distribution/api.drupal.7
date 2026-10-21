# Archive_Tar::_openRead()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 872–938 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L872-L938)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _openRead()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function _openRead()
    {
        if (strtolower(substr($this->_tarname, 0, 7)) == 'http://') {

            // ----- Look if a local copy need to be done
            if ($this->_temp_tarname == '') {
                $this->_temp_tarname = uniqid('tar') . '.tmp';
                if (!$v_file_from = @fopen($this->_tarname, 'rb')) {
                    $this->_error(
                        'Unable to open in read mode \''
                        . $this->_tarname . '\''
                    );
                    $this->_temp_tarname = '';
                    return false;
                }
                if (!$v_file_to = @fopen($this->_temp_tarname, 'wb')) {
                    $this->_error(
                        'Unable to open in write mode \''
                        . $this->_temp_tarname . '\''
                    );
                    $this->_temp_tarname = '';
                    return false;
                }
                while ($v_data = @fread($v_file_from, 1024)) {
                    @fwrite($v_file_to, $v_data);
                }
                @fclose($v_file_from);
                @fclose($v_file_to);
            }

            // ----- File to open if the local copy
            $v_filename = $this->_temp_tarname;
        } else {
            // ----- File to open if the normal Tar file

            $v_filename = $this->_tarname;
        }

        if ($this->_compress_type == 'gz' && function_exists('gzopen')) {
            $this->_file = @gzopen($v_filename, "rb");
        } else {
            if ($this->_compress_type == 'bz2' && function_exists('bzopen')) {
                $this->_file = @bzopen($v_filename, "r");
            } else {
                if ($this->_compress_type == 'lzma2' && function_exists('xzopen')) {
                    $this->_file = @xzopen($v_filename, "r");
                } else {
                    if ($this->_compress_type == 'none') {
                        $this->_file = @fopen($v_filename, "rb");
                    } else {
                        $this->_error(
                            'Unknown or missing compression type ('
                            . $this->_compress_type . ')'
                        );
                        return false;
                    }
                }
            }
        }

        if ($this->_file == 0) {
            $this->_error('Unable to open in read mode \'' . $v_filename . '\'');
            return false;
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
