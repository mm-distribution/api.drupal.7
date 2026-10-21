# template_preprocess_block()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 1016–1046 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L1016-L1046)
- **Module/theme:** block

## Signature

```php
function template_preprocess_block(&$variables)
```

## Documentation

```text
Processes variables for block.tpl.php.

Prepares the values passed to the theme_block function to be passed
into a pluggable template engine. Uses block properties to generate a
series of template file suggestions. If none are found, the default
block.tpl.php is used.

Most themes utilize their own copy of block.tpl.php. The default is located
inside "modules/block/block.tpl.php". Look in there for the full list of
variables.

The $variables array contains the following arguments:
- $block

@see block.tpl.php
```

## Code

```php
function template_preprocess_block(&$variables) {
  $block_counter = &drupal_static(__FUNCTION__, array());
  $variables['block'] = $variables['elements']['#block'];
  // All blocks get an independent counter for each region.
  if (!isset($block_counter[$variables['block']->region])) {
    $block_counter[$variables['block']->region] = 1;
  }
  // Same with zebra striping.
  $variables['block_zebra'] = ($block_counter[$variables['block']->region] % 2) ? 'odd' : 'even';
  $variables['block_id'] = $block_counter[$variables['block']->region]++;

  // Create the $content variable that templates expect.
  $variables['content'] = $variables['elements']['#children'];

  $variables['classes_array'][] = drupal_html_class('block-' . $variables['block']->module);

  $variables['theme_hook_suggestions'][] = 'block__' . $variables['block']->region;
  $variables['theme_hook_suggestions'][] = 'block__' . $variables['block']->module;
  // Hyphens (-) and underscores (_) play a special role in theme suggestions.
  // Theme suggestions should only contain underscores, because within
  // drupal_find_theme_templates(), underscores are converted to hyphens to
  // match template file names, and then converted back to underscores to match
  // pre-processing and other function names. So if your theme suggestion
  // contains a hyphen, it will end up as an underscore after this conversion,
  // and your function names won't be recognized. So, we need to convert
  // hyphens to underscores in block deltas for the theme suggestions.
  $variables['theme_hook_suggestions'][] = 'block__' . $variables['block']->module . '__' . strtr($variables['block']->delta, '-', '_');

  // Create a valid HTML ID and make sure it is unique.
  $variables['block_html_id'] = drupal_html_id('block-' . $variables['block']->module . '-' . $variables['block']->delta);
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
