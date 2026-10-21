# Archive_Tar::listContent()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 387–400 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L387-L400)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function listContent()
```

## Documentation

```text
@return array|int
```

## Code

```php
    public function listContent()
    {
        $v_list_detail = array();

        if ($this->_openRead()) {
            if (!$this->_extractList('', $v_list_detail, "list", '', '')) {
                unset($v_list_detail);
                $v_list_detail = 0;
            }
            $this->_close();
        }

        return $v_list_detail;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
