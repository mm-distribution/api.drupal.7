# update_selection_page()

- **Type:** Function
- **File:** [`update.php`](_file.md), lines 33–41 · [local source](../../source/update.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/update.php#L33-L41)

## Signature

```php
function update_selection_page()
```

## Documentation

```text
Renders a form with a list of available database updates.
```

## Code

```php
function update_selection_page() {
  drupal_set_title('Drupal database update');
  $elements = drupal_get_form('update_script_selection_form');
  $output = drupal_render($elements);

  update_task_list('select');

  return $output;
}
```

---
_Drupal 7.103 · [update.php](https://github.com/drupal/drupal/blob/7.103/update.php) · Licensed GPL-2.0-or-later (see LICENSE)._
