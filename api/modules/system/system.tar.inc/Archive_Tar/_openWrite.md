# Archive_Tar::_openWrite()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 834–867 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L834-L867)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _openWrite()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function _openWrite()
    {
        if ($this->_compress_type == 'gz' && function_exists('gzopen')) {
            $this->_file = @gzopen($this->_tarname, "wb9");
        } else {
            if ($this->_compress_type == 'bz2' && function_exists('bzopen')) {
                $this->_file = @bzopen($this->_tarname, "w");
            } else {
                if ($this->_compress_type == 'lzma2' && function_exists('xzopen')) {
                    $this->_file = @xzopen($this->_tarname, 'w');
                } else {
                    if ($this->_compress_type == 'none') {
                        $this->_file = @fopen($this->_tarname, "wb");
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
            $this->_error(
                'Unable to open in write mode \''
                . $this->_tarname . '\''
            );
            return false;
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
