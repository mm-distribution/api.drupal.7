# Archive_Tar::_error()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 803–807 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L803-L807)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _error($p_message)
```

## Documentation

```text
@param string $p_message
```

## Code

```php
    public function _error($p_message)
    {
        // Drupal change $this->error_object = $this->raiseError($p_message).
        throw new Exception($p_message);
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
