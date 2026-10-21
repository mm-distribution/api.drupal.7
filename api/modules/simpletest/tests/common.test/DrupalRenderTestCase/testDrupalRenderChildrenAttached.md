# DrupalRenderTestCase::testDrupalRenderChildrenAttached()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2218–2263 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2218-L2263)
- **Class:** [DrupalRenderTestCase](../DrupalRenderTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalRenderChildrenAttached()
```

## Documentation

```text
Test #attached functionality in children elements.
```

## Code

```php
  function testDrupalRenderChildrenAttached() {
    // The cache system is turned off for POST requests.
    $request_method = $_SERVER['REQUEST_METHOD'];
    $_SERVER['REQUEST_METHOD'] = 'GET';

    // Create an element with a child and subchild.  Each element loads a
    // different JavaScript file using #attached.
    $parent_js = drupal_get_path('module', 'user') . '/user.js';
    $child_js = drupal_get_path('module', 'forum') . '/forum.js';
    $subchild_js = drupal_get_path('module', 'book') . '/book.js';
    $element = array(
      '#type' => 'fieldset',
      '#cache' => array(
        'keys' => array('simpletest', 'drupal_render', 'children_attached'),
      ),
      '#attached' => array('js' => array($parent_js)),
      '#title' => 'Parent',
    );
    $element['child'] = array(
      '#type' => 'fieldset',
      '#attached' => array('js' => array($child_js)),
      '#title' => 'Child',
    );
    $element['child']['subchild'] = array(
      '#attached' => array('js' => array($subchild_js)),
      '#markup' => 'Subchild',
    );

    // Render the element and verify the presence of #attached JavaScript.
    drupal_render($element);
    $scripts = drupal_get_js();
    $this->assertTrue(strpos($scripts, $parent_js), 'The element #attached JavaScript was included.');
    $this->assertTrue(strpos($scripts, $child_js), 'The child #attached JavaScript was included.');
    $this->assertTrue(strpos($scripts, $subchild_js), 'The subchild #attached JavaScript was included.');

    // Load the element from cache and verify the presence of the #attached
    // JavaScript.
    drupal_static_reset('drupal_add_js');
    $this->assertTrue(drupal_render_cache_get($element), 'The element was retrieved from cache.');
    $scripts = drupal_get_js();
    $this->assertTrue(strpos($scripts, $parent_js), 'The element #attached JavaScript was included when loading from cache.');
    $this->assertTrue(strpos($scripts, $child_js), 'The child #attached JavaScript was included when loading from cache.');
    $this->assertTrue(strpos($scripts, $subchild_js), 'The subchild #attached JavaScript was included when loading from cache.');

    $_SERVER['REQUEST_METHOD'] = $request_method;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
