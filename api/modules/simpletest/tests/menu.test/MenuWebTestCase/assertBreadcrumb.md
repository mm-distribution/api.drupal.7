# MenuWebTestCase::assertBreadcrumb()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 36–103 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L36-L103)
- **Class:** [MenuWebTestCase](../MenuWebTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertBreadcrumb($goto, array $trail, $page_title = NULL, array $tree = array(), $last_active = TRUE)
```

## Documentation

```text
Assert that a given path shows certain breadcrumb links.

@param string $goto
  (optional) A system path to pass to DrupalWebTestCase::drupalGet().
@param array $trail
  An associative array whose keys are expected breadcrumb link paths and
  whose values are expected breadcrumb link texts (not sanitized).
@param string $page_title
  (optional) A page title to additionally assert via
  DrupalWebTestCase::assertTitle(). Without site name suffix.
@param array $tree
  (optional) An associative array whose keys are link paths and whose
  values are link titles (not sanitized) of an expected active trail in a
  menu tree output on the page.
@param $last_active
  (optional) Whether the last link in $tree is expected to be active (TRUE)
  or just to be in the active trail (FALSE).
```

## Code

```php
  protected function assertBreadcrumb($goto, array $trail, $page_title = NULL, array $tree = array(), $last_active = TRUE) {
    if (isset($goto)) {
      $this->drupalGet($goto);
    }
    // Compare paths with actual breadcrumb.
    $parts = $this->getParts();
    $pass = TRUE;
    foreach ($trail as $path => $title) {
      $url = url($path);
      $part = array_shift($parts);
      $pass = ($pass && $part['href'] === $url && $part['text'] === check_plain($title));
    }
    // No parts must be left, or an expected "Home" will always pass.
    $pass = ($pass && empty($parts));

    $this->assertTrue($pass, format_string('Breadcrumb %parts found on @path.', array(
      '%parts' => implode(' » ', $trail),
      '@path' => $this->getUrl(),
    )));

    // Additionally assert page title, if given.
    if (isset($page_title)) {
      $this->assertTitle(strtr('@title | Drupal', array('@title' => $page_title)));
    }

    // Additionally assert active trail in a menu tree output, if given.
    if ($tree) {
      end($tree);
      $active_link_path = key($tree);
      $active_link_title = array_pop($tree);
      $xpath = '';
      if ($tree) {
        $i = 0;
        foreach ($tree as $link_path => $link_title) {
          $part_xpath = (!$i ? '//' : '/following-sibling::ul/descendant::');
          $part_xpath .= 'li[contains(@class, :class)]/a[contains(@href, :href) and contains(text(), :title)]';
          $part_args = array(
            ':class' => 'active-trail',
            ':href' => url($link_path),
            ':title' => $link_title,
          );
          $xpath .= $this->buildXPathQuery($part_xpath, $part_args);
          $i++;
        }
        $elements = $this->xpath($xpath);
        $this->assertTrue(!empty($elements), 'Active trail to current page was found in menu tree.');

        // Append prefix for active link asserted below.
        $xpath .= '/following-sibling::ul/descendant::';
      }
      else {
        $xpath .= '//';
      }
      $xpath_last_active = ($last_active ? 'and contains(@class, :class-active)' : '');
      $xpath .= 'li[contains(@class, :class-trail)]/a[contains(@href, :href) ' . $xpath_last_active . 'and contains(text(), :title)]';
      $args = array(
        ':class-trail' => 'active-trail',
        ':class-active' => 'active',
        ':href' => url($active_link_path),
        ':title' => $active_link_title,
      );
      $elements = $this->xpath($xpath, $args);
      $this->assertTrue(!empty($elements), format_string('Active link %title was found in menu tree, including active trail links %tree.', array(
        '%title' => $active_link_title,
        '%tree' => implode(' » ', $tree),
      )));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
