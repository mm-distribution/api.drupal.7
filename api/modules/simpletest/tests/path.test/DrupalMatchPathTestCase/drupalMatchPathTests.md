# DrupalMatchPathTestCase::drupalMatchPathTests()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 55–126 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L55-L126)
- **Class:** [DrupalMatchPathTestCase](../DrupalMatchPathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
private function drupalMatchPathTests()
```

## Documentation

```text
Helper function for testDrupalMatchPath(): set up an array of test cases.

@return
  An array of test cases to cycle through.
```

## Code

```php
  private function drupalMatchPathTests() {
    return array(
      // Single absolute paths.
      'blog/1' => array(
        'blog/1' => TRUE,
        'blog/2' => FALSE,
        'test' => FALSE,
      ),
      // Single paths with wildcards.
      'blog/*' => array(
        'blog/1' => TRUE,
        'blog/2' => TRUE,
        'blog/3/edit' => TRUE,
        'blog/' => TRUE,
        'blog' => FALSE,
        'test' => FALSE,
      ),
      // Single paths with multiple wildcards.
      'node/*/revisions/*' => array(
        'node/1/revisions/3' => TRUE,
        'node/345/revisions/test' => TRUE,
        'node/23/edit' => FALSE,
        'test' => FALSE,
      ),
      // Single paths with '<front>'.
      '<front>' => array(
        $this->front => TRUE,
        "$this->front/" => FALSE,
        "$this->front/edit" => FALSE,
        'node' => FALSE,
        '' => FALSE,
      ),
      // Paths with both '<front>' and wildcards (should not work).
      '<front>/*' => array(
        $this->front => FALSE,
        "$this->front/" => FALSE,
        "$this->front/edit" => FALSE,
        'node/12' => FALSE,
        '' => FALSE,
      ),
      // Multiple paths with the \n delimiter.
      "node/*\nnode/*/edit" => array(
        'node/1' => TRUE,
        'node/view' => TRUE,
        'node/32/edit' => TRUE,
        'node/delete/edit' => TRUE,
        'node/50/delete' => TRUE,
        'test/example' => FALSE,
      ),
      // Multiple paths with the \r delimiter.
      "user/*\rblog/*" => array(
        'user/1' => TRUE,
        'blog/1' => TRUE,
        'user/1/blog/1' => TRUE,
        'user/blog' => TRUE,
        'test/example' => FALSE,
        'user' => FALSE,
        'blog' => FALSE,
      ),
      // Multiple paths with the \r\n delimiter.
      "test\r\n<front>" => array(
        'test' => TRUE,
        $this->front => TRUE,
        'example' => FALSE,
      ),
      // Test existing regular expressions (should be escaped).
      '[^/]+?/[0-9]' => array(
        'test/1' => FALSE,
        '[^/]+?/[0-9]' => TRUE,
      ),
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
