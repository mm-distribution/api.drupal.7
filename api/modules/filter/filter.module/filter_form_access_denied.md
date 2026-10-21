# filter_form_access_denied()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 993–996 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L993-L996)
- **Module/theme:** filter

## Signature

```php
function filter_form_access_denied($element)
```

## Documentation

```text
Render API callback: Hides the field value of 'text_format' elements.

To not break form processing and previews if a user does not have access to a
stored text format, the expanded form elements in filter_process_format() are
forced to take over the stored #default_values for 'value' and 'format'.
However, to prevent the unfiltered, original #value from being displayed to
the user, we replace it with a friendly notice here.

@see filter_process_format()
```

## Code

```php
function filter_form_access_denied($element) {
  $element['#value'] = t('This field has been disabled because you do not have sufficient permissions to edit it.');
  return $element;
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
