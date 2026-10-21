# BlockTemplateSuggestionsUnitTest::testBlockThemeHookSuggestions()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 730–753 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L730-L753)
- **Class:** [BlockTemplateSuggestionsUnitTest](../BlockTemplateSuggestionsUnitTest.md)
- **Module/theme:** block

## Signature

```php
function testBlockThemeHookSuggestions()
```

## Documentation

```text
Test if template_preprocess_block() handles the suggestions right.
```

## Code

```php
  function testBlockThemeHookSuggestions() {
    // Define block delta with underscore to be preprocessed
    $block1 = new stdClass();
    $block1->module = 'block';
    $block1->delta = 'underscore_test';
    $block1->region = 'footer';
    $variables1 = array();
    $variables1['elements']['#block'] = $block1;
    $variables1['elements']['#children'] = '';
    template_preprocess_block($variables1);
    $this->assertEqual($variables1['theme_hook_suggestions'], array('block__footer', 'block__block', 'block__block__underscore_test'), 'Found expected block suggestions for delta with underscore');

    // Define block delta with hyphens to be preprocessed. Hyphens should be
    // replaced with underscores.
    $block2 = new stdClass();
    $block2->module = 'block';
    $block2->delta = 'hyphen-test';
    $block2->region = 'footer';
    $variables2 = array();
    $variables2['elements']['#block'] = $block2;
    $variables2['elements']['#children'] = '';
    template_preprocess_block($variables2);
    $this->assertEqual($variables2['theme_hook_suggestions'], array('block__footer', 'block__block', 'block__block__hyphen_test'), 'Hyphens (-) in block delta were replaced by underscore (_)');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
