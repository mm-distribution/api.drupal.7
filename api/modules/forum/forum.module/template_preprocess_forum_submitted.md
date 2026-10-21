# template_preprocess_forum_submitted()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 1274–1277 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L1274-L1277)
- **Module/theme:** forum

## Signature

```php
function template_preprocess_forum_submitted(&$variables)
```

## Documentation

```text
Preprocesses variables for forum-submitted.tpl.php.

The submission information will be displayed in the forum list and topic
list.

@param $variables
  An array containing the following elements:
  - topic: The topic object.

@see forum-submitted.tpl.php
@see theme_forum_submitted()
```

## Code

```php
function template_preprocess_forum_submitted(&$variables) {
  $variables['author'] = isset($variables['topic']->uid) ? theme('username', array('account' => $variables['topic'])) : '';
  $variables['time'] = isset($variables['topic']->created) ? format_interval(REQUEST_TIME - $variables['topic']->created) : '';
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
