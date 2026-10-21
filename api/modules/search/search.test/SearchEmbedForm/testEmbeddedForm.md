# SearchEmbedForm::testEmbeddedForm()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1911–1941 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1911-L1941)
- **Class:** [SearchEmbedForm](../SearchEmbedForm.md)
- **Module/theme:** search

## Signature

```php
function testEmbeddedForm()
```

## Documentation

```text
Tests that the embedded form appears and can be submitted.
```

## Code

```php
  function testEmbeddedForm() {
    // First verify we can submit the form from the module's page.
    $this->drupalPost('search_embedded_form',
      array('name' => 'John'),
      t('Send away'));
    $this->assertText(t('Test form was submitted'), 'Form message appears');
    $count = variable_get('search_embedded_form_submitted', 0);
    $this->assertEqual($this->submit_count + 1, $count, 'Form submission count is correct');
    $this->submit_count = $count;

    // Now verify that we can see and submit the form from the search results.
    $this->drupalGet('search/node/' . $this->node->title);
    $this->assertText(t('Your name'), 'Form is visible');
    $this->drupalPost('search/node/' . $this->node->title,
      array('name' => 'John'),
      t('Send away'));
    $this->assertText(t('Test form was submitted'), 'Form message appears');
    $count = variable_get('search_embedded_form_submitted', 0);
    $this->assertEqual($this->submit_count + 1, $count, 'Form submission count is correct');
    $this->submit_count = $count;

    // Now verify that if we submit the search form, it doesn't count as
    // our form being submitted.
    $this->drupalPost('search',
      array('keys' => 'foo'),
      t('Search'));
    $this->assertNoText(t('Test form was submitted'), 'Form message does not appear');
    $count = variable_get('search_embedded_form_submitted', 0);
    $this->assertEqual($this->submit_count, $count, 'Form submission count is correct');
    $this->submit_count = $count;
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
