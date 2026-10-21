# RenderElementTypesTestCase::testHtmlTag()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 526–554 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L526-L554)
- **Class:** [RenderElementTypesTestCase](../RenderElementTypesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testHtmlTag()
```

## Documentation

```text
Tests system #type 'html_tag'.
```

## Code

```php
  function testHtmlTag() {
    $elements = array(
      // Test auto-closure meta tag generation.
      array(
        'name' => "#type 'html_tag' auto-closure meta tag generation",
        'value' => array(
          '#type' => 'html_tag',
          '#tag' => 'meta',
          '#attributes' => array(
            'name' => 'description',
            'content' => 'Drupal test',
          ),
        ),
        'expected' => '<meta name="description" content="Drupal test" />' . "\n",
      ),
      // Test title tag generation.
      array(
        'name' => "#type 'html_tag' title tag generation",
        'value' => array(
          '#type' => 'html_tag',
          '#tag' => 'title',
          '#value' => 'title test',
        ),
        'expected' => '<title>title test</title>' . "\n",
      ),
    );

    $this->assertElements($elements);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
