# ThemeDebugMarkupTestCase::testDebugOutput()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 629–669 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L629-L669)
- **Class:** [ThemeDebugMarkupTestCase](../ThemeDebugMarkupTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDebugOutput()
```

## Documentation

```text
Tests debug markup added to template output.
```

## Code

```php
  function testDebugOutput() {
    variable_set('theme_default', 'test_theme');
    // Enable the debug output.
    variable_set('theme_debug', TRUE);

    $registry = theme_get_registry();
    $extension = '.tpl.php';
    // Populate array of templates.
    $templates = drupal_find_theme_templates($registry, $extension, drupal_get_path('theme', 'test_theme'));
    $templates += drupal_find_theme_templates($registry, $extension, drupal_get_path('module', 'node'));

    // Create a node and test different features of the debug markup.
    $node = $this->drupalCreateNode();
    $this->drupalGet('node/' . $node->nid);
    $this->assertRaw('<!-- THEME DEBUG -->', 'Theme debug markup found in theme output when debug is enabled.');
    $this->assertRaw("CALL: theme('node')", 'Theme call information found.');
    $this->assertRaw('x node--1' . $extension . PHP_EOL . '   * node--page' . $extension . PHP_EOL . '   * node' . $extension, 'Suggested template files found in order and node ID specific template shown as current template.');
    $template_filename = $templates['node__1']['path'] . '/' . $templates['node__1']['template'] . $extension;
    $this->assertRaw("BEGIN OUTPUT from '$template_filename'", 'Full path to current template file found.');

    // Create another node and make sure the template suggestions shown in the
    // debug markup are correct.
    $node2 = $this->drupalCreateNode();
    $this->drupalGet('node/' . $node2->nid);
    $this->assertRaw('* node--2' . $extension . PHP_EOL . '   * node--page' . $extension . PHP_EOL . '   x node' . $extension, 'Suggested template files found in order and base template shown as current template.');

    // Create another node and make sure the template suggestions shown in the
    // debug markup are correct.
    $node3 = $this->drupalCreateNode();
    $build = array('#theme' => 'node__foo__bar');
    $build += node_view($node3);
    $output = drupal_render($build);
    $this->assertTrue(strpos($output, "CALL: theme('node__foo__bar')") !== FALSE, 'Theme call information found.');
    $this->assertTrue(strpos($output, '* node--foo--bar' . $extension . PHP_EOL . '   * node--foo' . $extension . PHP_EOL . '   * node--3' . $extension . PHP_EOL . '   * node--page' . $extension . PHP_EOL . '   x node' . $extension) !== FALSE, 'Suggested template files found in order and base template shown as current template.');

    // Disable theme debug.
    variable_set('theme_debug', FALSE);

    $this->drupalGet('node/' . $node->nid);
    $this->assertNoRaw('<!-- THEME DEBUG -->', 'Theme debug markup not found in theme output when debug is disabled.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
