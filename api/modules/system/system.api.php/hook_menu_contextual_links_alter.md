# hook_menu_contextual_links_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1561–1574 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1561-L1574)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_menu_contextual_links_alter(&$links, $router_item, $root_path)
```

## Documentation

```text
Alter contextual links before they are rendered.

This hook is invoked by menu_contextual_links(). The system-determined
contextual links are passed in by reference. Additional links may be added
or existing links can be altered.

Each contextual link must at least contain:
- title: The localized title of the link.
- href: The system path to link to.
- localized_options: An array of options to pass to url().

@param $links
  An associative array containing contextual links for the given $root_path,
  as described above. The array keys are used to build CSS class names for
  contextual links and must therefore be unique for each set of contextual
  links.
@param $router_item
  The menu router item belonging to the $root_path being requested.
@param $root_path
  The (parent) path that has been requested to build contextual links for.
  This is a normalized path, which means that an originally passed path of
  'node/123' became 'node/%'.

@see hook_contextual_links_view_alter()
@see menu_contextual_links()
@see hook_menu()
@see contextual_preprocess()
```

## Code

```php
function hook_menu_contextual_links_alter(&$links, $router_item, $root_path) {
  // Add a link to all contextual links for nodes.
  if ($root_path == 'node/%') {
    $links['foo'] = array(
      'title' => t('Do fu'),
      'href' => 'foo/do',
      'localized_options' => array(
        'query' => array(
          'foo' => 'bar',
        ),
      ),
    );
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_menu_contextual_links_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
