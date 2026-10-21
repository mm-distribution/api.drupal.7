# Archive_Tar::_writeBlock()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1053–1101 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1053-L1101)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _writeBlock($p_binary_data, $p_len = null)
```

## Documentation

```text
@param mixed $p_binary_data
@param integer $p_len
@return bool
```

## Code

```php
    public function _writeBlock($p_binary_data, $p_len = null)
    {
        if (is_resource($this->_file)) {
            if ($p_len === null) {
                if ($this->_compress_type == 'gz') {
                    @gzputs($this->_file, $p_binary_data);
                } else {
                    if ($this->_compress_type == 'bz2') {
                        @bzwrite($this->_file, $p_binary_data);
                    } else {
                        if ($this->_compress_type == 'lzma2') {
                            @xzwrite($this->_file, $p_binary_data);
                        } else {
                            if ($this->_compress_type == 'none') {
                                @fputs($this->_file, $p_binary_data);
                            } else {
                                $this->_error(
                                    'Unknown or missing compression type ('
                                    . $this->_compress_type . ')'
                                );
                            }
                        }
                    }
                }
            } else {
                if ($this->_compress_type == 'gz') {
                    @gzputs($this->_file, $p_binary_data, $p_len);
                } else {
                    if ($this->_compress_type == 'bz2') {
                        @bzwrite($this->_file, $p_binary_data, $p_len);
                    } else {
                        if ($this->_compress_type == 'lzma2') {
                            @xzwrite($this->_file, $p_binary_data, $p_len);
                        } else {
                            if ($this->_compress_type == 'none') {
                                @fputs($this->_file, $p_binary_data, $p_len);
                            } else {
                                $this->_error(
                                    'Unknown or missing compression type ('
                                    . $this->_compress_type . ')'
                                );
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
