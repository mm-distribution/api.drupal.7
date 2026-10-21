# TaxonomyTermTestCase

- **Type:** Class
- **File:** [`modules/taxonomy/taxonomy.test`](_file.md), lines 531–1072 · [local source](../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L531-L1072)
- **Module/theme:** taxonomy

## Signature

```php
class TaxonomyTermTestCase extends TaxonomyWebTestCase
```

## Documentation

```text
Tests for taxonomy term functions.
```

## Properties

### $vocabulary

```php
protected $vocabulary;
```

### $instance

```php
protected $instance;
```

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](TaxonomyTermTestCase/getInfo.md)
- [setUp()](TaxonomyTermTestCase/setUp.md)
- [testTaxonomyTermHierarchy()](TaxonomyTermTestCase/testTaxonomyTermHierarchy.md) — Test terms in a single and multiple hierarchy.
- [testTaxonomyNode()](TaxonomyTermTestCase/testTaxonomyNode.md) — Test that hook_node_$op implementations work correctly.
- [testNodeTermCreationAndDeletion()](TaxonomyTermTestCase/testNodeTermCreationAndDeletion.md) — Test term creation with a free-tagging vocabulary from the node form.
- [testTermAutocompletion()](TaxonomyTermTestCase/testTermAutocompletion.md) — Tests term autocompletion edge cases with slashes in the names.
- [testTermInterface()](TaxonomyTermTestCase/testTermInterface.md) — Save, edit and delete a term using the user interface.
- [testTermReorder()](TaxonomyTermTestCase/testTermReorder.md) — Save, edit and delete a term using the user interface.
- [testTermMultipleParentsInterface()](TaxonomyTermTestCase/testTermMultipleParentsInterface.md) — Test saving a term with multiple parents through the UI.
- [testTaxonomyGetTermByName()](TaxonomyTermTestCase/testTaxonomyGetTermByName.md) — Test taxonomy_get_term_by_name().
- [testTaxonomySelectNodesAlter()](TaxonomyTermTestCase/testTaxonomySelectNodesAlter.md) — Tests that taxonomy term detail page is working even after the default taxonomy_select_nodes() query is altered.
- [testTaxonomyTermsOverviewPage()](TaxonomyTermTestCase/testTaxonomyTermsOverviewPage.md) — Test multiple forms on taxonomy terms overview page.

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
