# TaxonomyTermTestCase::testTaxonomyTermsOverviewPage()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1050–1070 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1050-L1070)
- **Class:** [TaxonomyTermTestCase](../TaxonomyTermTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function testTaxonomyTermsOverviewPage()
```

## Documentation

```text
Test multiple forms on taxonomy terms overview page.
```

## Code

```php
  function testTaxonomyTermsOverviewPage() {
    // Enable block with custom form on taxonomy terms overview page.
    module_enable(array('taxonomy_test'));

    $this->drupalLogout();
    $admin_user1 = $this->drupalCreateUser(array('administer taxonomy', 'administer blocks', 'bypass node access'));
    $this->drupalLogin($admin_user1);

    $this->createTerm($this->vocabulary);
    $this->createTerm($this->vocabulary);

    $edit = array();
    $edit['blocks[taxonomy_test_test_block_form][region]'] = 'header';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    $this->drupalGet('admin/structure/taxonomy/' . $this->vocabulary->machine_name);
    $this->assertText('Simple form', 'Block successfully being displayed on the page.');

    // Try to submit the custom form to verify there are no errors.
    $this->drupalPost(NULL, array(), t('Submit'));
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
