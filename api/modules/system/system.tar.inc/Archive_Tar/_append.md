# Archive_Tar::_append()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 2475–2488 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L2475-L2488)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function _append($p_filelist, $p_add_dir = '', $p_remove_dir = '')
```

## Documentation

```text
@param $p_filelist
@param string $p_add_dir
@param string $p_remove_dir
@return bool
```

## Code

```php
    public function _append($p_filelist, $p_add_dir = '', $p_remove_dir = '')
    {
        if (!$this->_openAppend()) {
            return false;
        }

        if ($this->_addList($p_filelist, $p_add_dir, $p_remove_dir)) {
            $this->_writeFooter();
        }

        $this->_close();

        return true;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
