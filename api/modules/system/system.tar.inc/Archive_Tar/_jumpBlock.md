# Archive_Tar::_jumpBlock()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1138–1173 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1138-L1173)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _jumpBlock($p_len = null)
```

## Documentation

```text
@param null $p_len
@return bool
```

## Code

```php
    public function _jumpBlock($p_len = null)
    {
        if (is_resource($this->_file)) {
            if ($p_len === null) {
                $p_len = 1;
            }

            if ($this->_compress_type == 'gz') {
                @gzseek($this->_file, gztell($this->_file) + ($p_len * 512));
            } else {
                if ($this->_compress_type == 'bz2') {
                    // ----- Replace missing bztell() and bzseek()
                    for ($i = 0; $i < $p_len; $i++) {
                        $this->_readBlock();
                    }
                } else {
                    if ($this->_compress_type == 'lzma2') {
                        // ----- Replace missing xztell() and xzseek()
                        for ($i = 0; $i < $p_len; $i++) {
                            $this->_readBlock();
                        }
                    } else {
                        if ($this->_compress_type == 'none') {
                            @fseek($this->_file, $p_len * 512, SEEK_CUR);
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
        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
