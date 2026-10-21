# SearchBlockTestCase::testBlock()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 627–687 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L627-L687)
- **Class:** [SearchBlockTestCase](../SearchBlockTestCase.md)
- **Module/theme:** search

## Signature

```php
function testBlock()
```

## Documentation

```text
Test that the search block form works correctly.
```

## Code

```php
  function testBlock() {
    // Enable the block, and place it in the 'content' region so that it isn't
    // hidden on 404 pages.
    $edit = array('blocks[search_form][region]' => 'content');
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Test a normal search via the block form, from the front page.
    $terms = array('search_block_form' => 'test');
    $this->drupalPost('node', $terms, t('Search'));
    $this->assertText('Your search yielded no results');

    // Test a search from the block on a 404 page.
    $this->drupalGet('foo');
    $this->assertResponse(404);
    $this->drupalPost(NULL, $terms, t('Search'));
    $this->assertResponse(200);
    $this->assertText('Your search yielded no results');

    // Test a search from the block when it doesn't appear on the search page.
    $edit = array('pages' => 'search');
    $this->drupalPost('admin/structure/block/manage/search/form/configure', $edit, t('Save block'));
    $this->drupalPost('node', $terms, t('Search'));
    $this->assertText('Your search yielded no results');

    // Confirm that the user is redirected to the search page.
    $this->assertEqual(
      $this->getUrl(),
      url('search/node/' . $terms['search_block_form'], array('absolute' => TRUE)),
      'Redirected to correct url.'
    );

    // Test an empty search via the block form, from the front page.
    $terms = array('search_block_form' => '');
    $this->drupalPost('node', $terms, t('Search'));
    $this->assertText('Please enter some keywords');

    // Confirm that the user is redirected to the search page, when form is submitted empty.
    $this->assertEqual(
      $this->getUrl(),
      url('search/node/', array('absolute' => TRUE)),
      'Redirected to correct url.'
    );

    // Test that after entering a too-short keyword in the form, you can then
    // search again with a longer keyword. First test using the block form.
    $terms = array('search_block_form' => 'a');
    $this->drupalPost('node', $terms, t('Search'));
    $this->assertText('You must include at least one positive keyword with 3 characters or more');
    $terms = array('search_block_form' => 'foo');
    $this->drupalPost(NULL, $terms, t('Search'));
    $this->assertNoText('You must include at least one positive keyword with 3 characters or more');
    $this->assertText('Your search yielded no results');

    // Same test again, using the search page form for the second search this time.
    $terms = array('search_block_form' => 'a');
    $this->drupalPost('node', $terms, t('Search'));
    $terms = array('keys' => 'foo');
    $this->drupalPost(NULL, $terms, t('Search'));
    $this->assertNoText('You must include at least one positive keyword with 3 characters or more');
    $this->assertText('Your search yielded no results');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
