# Archive_Tar::_isArchive()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 822–829 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L822-L829)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _isArchive($p_filename = null)
```

## Documentation

```text
@param string $p_filename
@return bool
```

## Code

```php
    public function _isArchive($p_filename = null)
    {
        if ($p_filename == null) {
            $p_filename = $this->_tarname;
        }
        clearstatcache();
        return @is_file($p_filename) && !@is_link($p_filename);
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
