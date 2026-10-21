# filter_admin_format_page()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 123–132 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L123-L132)
- **Module/theme:** filter

## Signature

```php
function filter_admin_format_page($format = NULL)
```

## Documentation

```text
Page callback: Displays the text format add/edit form.

@param object|null $format
  (optional) An object representing a format, with the following properties:
  - format: A machine-readable name representing the ID of the text format
    to save. If this corresponds to an existing text format, that format
    will be updated; otherwise, a new format will be created.
  - name: The title of the text format.
  - cache: (optional) An integer indicating whether the text format is
    cacheable (1) or not (0). Defaults to 1.
  - status: (optional) An integer indicating whether the text format is
    enabled (1) or not (0). Defaults to 1.
  - weight: (optional) The weight of the text format, which controls its
    placement in text format lists. If omitted, the weight is set to 0.
    Defaults to NULL.

@return
  A form array.

@see filter_menu()
```

## Code

```php
function filter_admin_format_page($format = NULL) {
  if (!isset($format->name)) {
    drupal_set_title(t('Add text format'));
    $format = (object) array(
      'format' => NULL,
      'name' => '',
    );
  }
  return drupal_get_form('filter_admin_format_form', $format);
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
