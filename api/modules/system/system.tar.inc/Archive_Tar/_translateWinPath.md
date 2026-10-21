# Archive_Tar::_translateWinPath()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 2577–2592 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L2577-L2592)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _translateWinPath($p_path, $p_remove_disk_letter = true)
```

## Documentation

```text
@param $p_path
@param bool $p_remove_disk_letter
@return string
```

## Code

```php
    public function _translateWinPath($p_path, $p_remove_disk_letter = true)
    {
        if (defined('OS_WINDOWS') && OS_WINDOWS) {
            // ----- Look for potential disk letter
            if (($p_remove_disk_letter)
                && (($v_position = strpos($p_path, ':')) != false)
            ) {
                $p_path = substr($p_path, $v_position + 1);
            }
            // ----- Change potential windows directory separator
            if ((strpos($p_path, '\\') > 0) || (substr($p_path, 0, 1) == '\\')) {
                $p_path = strtr($p_path, '\\', '/');
            }
        }
        return $p_path;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
