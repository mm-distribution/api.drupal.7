# search_forms()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 1349–1355 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L1349-L1355)
- **Module/theme:** search
- **Implements:** [hook_forms()](../../system/system.api.php/hook_forms.md)

## Signature

```php
function search_forms()
```

## Documentation

```text
Implements hook_forms().
```

## Code

```php
function search_forms() {
  $forms['search_block_form']= array(
    'callback' => 'search_box',
    'callback arguments' => array('search_block_form'),
  );
  return $forms;
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
