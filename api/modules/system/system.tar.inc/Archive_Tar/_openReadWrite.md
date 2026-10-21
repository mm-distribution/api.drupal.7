# Archive_Tar::_openReadWrite()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 943–984 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L943-L984)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _openReadWrite()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function _openReadWrite()
    {
        if ($this->_compress_type == 'gz') {
            $this->_file = @gzopen($this->_tarname, "r+b");
        } else {
            if ($this->_compress_type == 'bz2') {
                $this->_error(
                    'Unable to open bz2 in read/write mode \''
                    . $this->_tarname . '\' (limitation of bz2 extension)'
                );
                return false;
            } else {
                if ($this->_compress_type == 'lzma2') {
                    $this->_error(
                        'Unable to open lzma2 in read/write mode \''
                        . $this->_tarname . '\' (limitation of lzma2 extension)'
                    );
                    return false;
                } else {
                    if ($this->_compress_type == 'none') {
                        $this->_file = @fopen($this->_tarname, "r+b");
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
                'Unable to open in read/write mode \''
                . $this->_tarname . '\''
            );
            return false;
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
