# CascadingStylesheetsTestCase::testRenderInlineFullPage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 892–917 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L892-L917)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRenderInlineFullPage()
```

## Documentation

```text
Tests rendering inline stylesheets through a full page request.
```

## Code

```php
  function testRenderInlineFullPage() {
    $css = 'body { font-size: 254px; }';
    // Inline CSS is minified unless 'preprocess' => FALSE is passed as a
    // drupal_add_css() option.
    $expected = 'body{font-size:254px;}';

    // Create a node, using the PHP filter that tests drupal_add_css().
    $php_format_id = 'php_code';
    $settings = array(
      'type' => 'page',
      'body' => array(
        LANGUAGE_NONE => array(
          array(
            'value' => t('This tests the inline CSS!') . "<?php drupal_add_css('$css', 'inline'); ?>",
            'format' => $php_format_id,
          ),
        ),
      ),
      'promote' => 1,
    );
    $node = $this->drupalCreateNode($settings);

    // Fetch the page.
    $this->drupalGet('node/' . $node->nid);
    $this->assertRaw($expected, 'Inline stylesheets appear in the full page rendering.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
