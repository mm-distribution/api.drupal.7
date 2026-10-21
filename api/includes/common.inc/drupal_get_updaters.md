# drupal_get_updaters()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 8649–8657 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L8649-L8657)

## Signature

```php
function drupal_get_updaters()
```

## Documentation

```text
Assembles the Drupal Updater registry.

An Updater is a class that knows how to update various parts of the Drupal
file system, for example to update modules that have newer releases, or to
install a new theme.

@return
  The Drupal Updater class registry.

@see hook_updater_info()
@see hook_updater_info_alter()
```

## Code

```php
function drupal_get_updaters() {
  $updaters = &drupal_static(__FUNCTION__);
  if (!isset($updaters)) {
    $updaters = module_invoke_all('updater_info');
    drupal_alter('updater_info', $updaters);
    uasort($updaters, 'drupal_sort_weight');
  }
  return $updaters;
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
