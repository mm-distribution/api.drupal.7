# Archive_Tar::_dirCheck()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 2498–2520 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L2498-L2520)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _dirCheck($p_dir)
```

## Documentation

```text
Check if a directory exists and create it (including parent
dirs) if not.

@param string $p_dir directory to check

@return bool true if the directory exists or was created
```

## Code

```php
    public function _dirCheck($p_dir)
    {
        clearstatcache();
        if ((@is_dir($p_dir)) || ($p_dir == '')) {
            return true;
        }

        $p_parent_dir = dirname($p_dir);

        if (($p_parent_dir != $p_dir) &&
            ($p_parent_dir != '') &&
            (!$this->_dirCheck($p_parent_dir))
        ) {
            return false;
        }

        if (!@mkdir($p_dir, 0775)) {
            $this->_error("Unable to create directory '$p_dir'");
            return false;
        }

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
