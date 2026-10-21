# Archive_Tar::_pathReduction()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 2530–2570 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L2530-L2570)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
private function _pathReduction($p_dir)
```

## Documentation

```text
Compress path by changing for example "/dir/foo/../bar" to "/dir/bar",
rand emove double slashes.

@param string $p_dir path to reduce

@return string reduced path
```

## Code

```php
    private function _pathReduction($p_dir)
    {
        $v_result = '';

        // ----- Look for not empty path
        if ($p_dir != '') {
            // ----- Explode path by directory names
            $v_list = explode('/', $p_dir);

            // ----- Study directories from last to first
            for ($i = sizeof($v_list) - 1; $i >= 0; $i--) {
                // ----- Look for current path
                if ($v_list[$i] == ".") {
                    // ----- Ignore this directory
                    // Should be the first $i=0, but no check is done
                } else {
                    if ($v_list[$i] == "..") {
                        // ----- Ignore it and ignore the $i-1
                        $i--;
                    } else {
                        if (($v_list[$i] == '')
                            && ($i != (sizeof($v_list) - 1))
                            && ($i != 0)
                        ) {
                            // ----- Ignore only the double '//' in path,
                            // but not the first and last /
                        } else {
                            $v_result = $v_list[$i] . ($i != (sizeof($v_list) - 1) ? '/'
                                    . $v_result : '');
                        }
                    }
                }
            }
        }

        if (defined('OS_WINDOWS') && OS_WINDOWS) {
            $v_result = strtr($v_result, '\\', '/');
        }

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
