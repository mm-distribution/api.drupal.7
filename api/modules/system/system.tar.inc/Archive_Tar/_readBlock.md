# Archive_Tar::_readBlock()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1106–1132 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1106-L1132)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _readBlock()
```

## Documentation

```text
@return null|string
```

## Code

```php
    public function _readBlock()
    {
        $v_block = null;
        if (is_resource($this->_file)) {
            if ($this->_compress_type == 'gz') {
                $v_block = @gzread($this->_file, 512);
            } else {
                if ($this->_compress_type == 'bz2') {
                    $v_block = @bzread($this->_file, 512);
                } else {
                    if ($this->_compress_type == 'lzma2') {
                        $v_block = @xzread($this->_file, 512);
                    } else {
                        if ($this->_compress_type == 'none') {
                            $v_block = @fread($this->_file, 512);
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
        return $v_block;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
