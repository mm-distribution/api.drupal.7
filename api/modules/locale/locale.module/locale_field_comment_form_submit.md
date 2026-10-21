# locale_field_comment_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 419–421 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L419-L421)
- **Module/theme:** locale

## Signature

```php
function locale_field_comment_form_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for comment_form().

This submit handler needs to run before entity_form_submit_build_entity()
is invoked by comment_form_submit_build_comment(), because it alters the
values of attached fields.
```

## Code

```php
function locale_field_comment_form_submit($form, &$form_state) {
  locale_field_entity_form_submit('comment', $form, $form_state);
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
