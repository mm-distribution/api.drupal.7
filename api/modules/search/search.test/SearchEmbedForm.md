# SearchEmbedForm

- **Type:** Class
- **File:** [`modules/search/search.test`](_file.md), lines 1871–1942 · [local source](../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1871-L1942)
- **Module/theme:** search

## Signature

```php
class SearchEmbedForm extends DrupalWebTestCase
```

## Documentation

```text
Tests that we can embed a form in search results and submit it.
```

## Properties

### $node

```php
public $node;
```

```text
Node used for testing.
```

### $submit_count

```php
public $submit_count = 0;
```

```text
Count of how many times the form has been submitted.
```

## Methods (derived index)

- [getInfo()](SearchEmbedForm/getInfo.md)
- [setUp()](SearchEmbedForm/setUp.md)
- [testEmbeddedForm()](SearchEmbedForm/testEmbeddedForm.md) — Tests that the embedded form appears and can be submitted.

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
