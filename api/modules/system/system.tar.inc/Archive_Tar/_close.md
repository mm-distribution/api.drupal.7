# Archive_Tar::_close()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 989–1025 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L989-L1025)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _close()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function _close()
    {
        //if (isset($this->_file)) {
        if (is_resource($this->_file)) {
            if ($this->_compress_type == 'gz') {
                @gzclose($this->_file);
            } else {
                if ($this->_compress_type == 'bz2') {
                    @bzclose($this->_file);
                } else {
                    if ($this->_compress_type == 'lzma2') {
                        @xzclose($this->_file);
                    } else {
                        if ($this->_compress_type == 'none') {
                            @fclose($this->_file);
                        } else {
                            $this->_error(
                                'Unknown or missing compression type ('
                                . $this->_compress_type . ')'
                            );
                        }
                    }
                }
            }

            $this->_file = 0;
        }

        // ----- Look if a local copy need to be erase
        // Note that it might be interesting to keep the url for a time : ToDo
        if ($this->_temp_tarname != '') {
            @drupal_unlink($this->_temp_tarname);
            $this->_temp_tarname = '';
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
