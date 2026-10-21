# Archive_Tar::__destruct()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 279–286 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L279-L286)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function __destruct()
```

## Documentation

_No docblock in source._

## Code

```php
    public function __destruct()
    {
        $this->_close();
        // ----- Look for a local copy to delete
        if ($this->_temp_tarname != '' && (bool) preg_match('/^tar[[:alnum:]]*\.tmp$/', $this->_temp_tarname)) {
            @drupal_unlink($this->_temp_tarname);
        }
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
