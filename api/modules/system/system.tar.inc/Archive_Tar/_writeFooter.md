# Archive_Tar::_writeFooter()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 1178–1186 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L1178-L1186)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _writeFooter()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function _writeFooter()
    {
        if (is_resource($this->_file)) {
            // ----- Write the last 0 filled block for end of archive
            $v_binary_data = pack('a1024', '');
            $this->_writeBlock($v_binary_data);
        }
        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
