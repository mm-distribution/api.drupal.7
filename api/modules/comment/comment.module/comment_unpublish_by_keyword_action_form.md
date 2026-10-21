# comment_unpublish_by_keyword_action_form()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2656–2665 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2656-L2665)
- **Module/theme:** comment
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function comment_unpublish_by_keyword_action_form($context)
```

## Documentation

```text
Form builder; Prepare a form for blacklisted keywords.

@ingroup forms
@see comment_unpublish_by_keyword_action()
@see comment_unpublish_by_keyword_action_submit()
```

## Code

```php
function comment_unpublish_by_keyword_action_form($context) {
  $form['keywords'] = array(
    '#title' => t('Keywords'),
    '#type' => 'textarea',
    '#description' => t('The comment will be unpublished if it contains any of the phrases above. Use a case-sensitive, comma-separated list of phrases. Example: funny, bungee jumping, "Company, Inc."'),
    '#default_value' => isset($context['keywords']) ? drupal_implode_tags($context['keywords']) : '',
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
