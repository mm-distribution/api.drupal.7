# ThemeLinksTest::testDrupalPreRenderLinks()

- **Type:** Method
- **File:** [`modules/simpletest/tests/theme.test`](../_file.md), lines 308–401 · [local source](../../../../../../source/modules/simpletest/tests/theme.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test#L308-L401)
- **Class:** [ThemeLinksTest](../ThemeLinksTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalPreRenderLinks()
```

## Documentation

```text
Test the use of drupal_pre_render_links() on a nested array of links.
```

## Code

```php
  function testDrupalPreRenderLinks() {
    // Define the base array to be rendered, containing a variety of different
    // kinds of links.
    $base_array = array(
      '#theme' => 'links',
      '#pre_render' => array('drupal_pre_render_links'),
      '#links' => array(
        'parent_link' => array(
          'title' => 'Parent link original',
          'href' => 'parent-link-original',
        ),
      ),
      'first_child' => array(
        '#theme' => 'links',
        '#links' => array(
          // This should be rendered if 'first_child' is rendered separately,
          // but ignored if the parent is being rendered (since it duplicates
          // one of the parent's links).
          'parent_link' => array(
            'title' => 'Parent link copy',
            'href' => 'parent-link-copy',
          ),
          // This should always be rendered.
          'first_child_link' => array(
            'title' => 'First child link',
            'href' => 'first-child-link',
          ),
        ),
      ),
      // This should always be rendered as part of the parent.
      'second_child' => array(
        '#theme' => 'links',
        '#links' => array(
          'second_child_link' => array(
            'title' => 'Second child link',
            'href' => 'second-child-link',
          ),
        ),
      ),
      // This should never be rendered, since the user does not have access to
      // it.
      'third_child' => array(
        '#theme' => 'links',
        '#links' => array(
          'third_child_link' => array(
            'title' => 'Third child link',
            'href' => 'third-child-link',
          ),
        ),
        '#access' => FALSE,
      ),
    );

    // Start with a fresh copy of the base array, and try rendering the entire
    // thing. We expect a single <ul> with appropriate links contained within
    // it.
    $render_array = $base_array;
    $html = drupal_render($render_array);
    $dom = new DOMDocument();
    $dom->loadHTML($html);
    $this->assertEqual($dom->getElementsByTagName('ul')->length, 1, 'One "ul" tag found in the rendered HTML.');
    $list_elements = $dom->getElementsByTagName('li');
    $this->assertEqual($list_elements->length, 3, 'Three "li" tags found in the rendered HTML.');
    $this->assertEqual($list_elements->item(0)->nodeValue, 'Parent link original', 'First expected link found.');
    $this->assertEqual($list_elements->item(1)->nodeValue, 'First child link', 'Second expected link found.');
    $this->assertEqual($list_elements->item(2)->nodeValue, 'Second child link', 'Third expected link found.');
    $this->assertIdentical(strpos($html, 'Parent link copy'), FALSE, '"Parent link copy" link not found.');
    $this->assertIdentical(strpos($html, 'Third child link'), FALSE, '"Third child link" link not found.');

    // Now render 'first_child', followed by the rest of the links, and make
    // sure we get two separate <ul>'s with the appropriate links contained
    // within each.
    $render_array = $base_array;
    $child_html = drupal_render($render_array['first_child']);
    $parent_html = drupal_render($render_array);
    // First check the child HTML.
    $dom = new DOMDocument();
    $dom->loadHTML($child_html);
    $this->assertEqual($dom->getElementsByTagName('ul')->length, 1, 'One "ul" tag found in the rendered child HTML.');
    $list_elements = $dom->getElementsByTagName('li');
    $this->assertEqual($list_elements->length, 2, 'Two "li" tags found in the rendered child HTML.');
    $this->assertEqual($list_elements->item(0)->nodeValue, 'Parent link copy', 'First expected link found.');
    $this->assertEqual($list_elements->item(1)->nodeValue, 'First child link', 'Second expected link found.');
    // Then check the parent HTML.
    $dom = new DOMDocument();
    $dom->loadHTML($parent_html);
    $this->assertEqual($dom->getElementsByTagName('ul')->length, 1, 'One "ul" tag found in the rendered parent HTML.');
    $list_elements = $dom->getElementsByTagName('li');
    $this->assertEqual($list_elements->length, 2, 'Two "li" tags found in the rendered parent HTML.');
    $this->assertEqual($list_elements->item(0)->nodeValue, 'Parent link original', 'First expected link found.');
    $this->assertEqual($list_elements->item(1)->nodeValue, 'Second child link', 'Second expected link found.');
    $this->assertIdentical(strpos($parent_html, 'First child link'), FALSE, '"First child link" link not found.');
    $this->assertIdentical(strpos($parent_html, 'Third child link'), FALSE, '"Third child link" link not found.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/theme.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/theme.test) · Licensed GPL-2.0-or-later (see LICENSE)._
