# Archive_Tar::extract()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 379–382 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L379-L382)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function extract($p_path = '', $p_preserve = false, $p_symlinks = true)
```

## Documentation

```text
@param string $p_path
@param bool $p_preserve
@param bool $p_symlinks
@return bool
```

## Code

```php
    public function extract($p_path = '', $p_preserve = false, $p_symlinks = true)
    {
        return $this->extractModify($p_path, '', $p_preserve, $p_symlinks);
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
