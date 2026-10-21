# locale_block_view()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 1040–1054 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L1040-L1054)
- **Module/theme:** locale
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function locale_block_view($type)
```

## Documentation

```text
Implements hook_block_view().

Displays a language switcher. Only show if we have at least two languages.
```

## Code

```php
function locale_block_view($type) {
  if (drupal_multilingual()) {
    $path = drupal_is_front_page() ? '<front>' : $_GET['q'];
    $links = language_negotiation_get_switch_links($type, $path);

    if (isset($links->links)) {
      drupal_add_css(drupal_get_path('module', 'locale') . '/locale.css');
      $class = "language-switcher-{$links->provider}";
      $variables = array('links' => $links->links, 'attributes' => array('class' => array($class)));
      $block['content'] = theme('links__locale_block', $variables);
      $block['subject'] = t('Languages');
      return $block;
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
