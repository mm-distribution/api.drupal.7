# drupal_get_filetransfer_info()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8669–8693 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8669-L8693)

## Signature

```php
function drupal_get_filetransfer_info()
```

## Documentation

```text
Assembles the Drupal FileTransfer registry.

@return
  The Drupal FileTransfer class registry.

@see FileTransfer
@see hook_filetransfer_info()
@see hook_filetransfer_info_alter()
```

## Code

```php
function drupal_get_filetransfer_info() {
  $info = &drupal_static(__FUNCTION__);
  if (!isset($info)) {
    // Since we have to manually set the 'file path' default for each
    // module separately, we can't use module_invoke_all().
    $info = array();
    foreach (module_implements('filetransfer_info') as $module) {
      $function = $module . '_filetransfer_info';
      if (function_exists($function)) {
        $result = $function();
        if (isset($result) && is_array($result)) {
          foreach ($result as &$values) {
            if (empty($values['file path'])) {
              $values['file path'] = drupal_get_path('module', $module);
            }
          }
          $info = array_merge_recursive($info, $result);
        }
      }
    }
    drupal_alter('filetransfer_info', $info);
    uasort($info, 'drupal_sort_weight');
  }
  return $info;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
