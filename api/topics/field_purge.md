# Field API bulk data deletion

- **Topic id:** `field_purge`
- **Defined in:** [`modules/field/field.crud.inc`](../modules/field/field.crud.inc/_file.md), line 813 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.crud.inc#L813)

## Documentation

```text
@defgroup field_purge Field API bulk data deletion
@{
Clean up after Field API bulk deletion operations.

Field API provides functions for deleting data attached to individual
entities as well as deleting entire fields or field instances in a single
operation.

Deleting field data items for an entity with field_attach_delete() involves
three separate operations:
- Invoking the Field Type API hook_field_delete() for each field on the
entity. The hook for each field type receives the entity and the specific
field being deleted. A file field module might use this hook to delete
uploaded files from the filesystem.
- Invoking the Field Storage API hook_field_storage_delete() to remove
data from the primary field storage. The hook implementation receives the
entity being deleted and deletes data for all of the entity's bundle's
fields.
- Invoking the global Field Attach API hook_field_attach_delete() for all
modules that implement it. Each hook implementation receives the entity
being deleted and can operate on whichever subset of the entity's bundle's
fields it chooses to.

These hooks are invoked immediately when field_attach_delete() is
called. Similar operations are performed for field_attach_delete_revision().

When a field, bundle, or field instance is deleted, it is not practical to
invoke these hooks immediately on every affected entity in a single page
request; there could be thousands or millions of them. Instead, the
appropriate field data items, instances, and/or fields are marked as deleted
so that subsequent load or query operations will not return them. Later, a
separate process cleans up, or "purges", the marked-as-deleted data by going
through the three-step process described above and, finally, removing
deleted field and instance records.

Purging field data is made somewhat tricky by the fact that, while
field_attach_delete() has a complete entity to pass to the various deletion
hooks, the Field API purge process only has the field data it has previously
stored. It cannot reconstruct complete original entities to pass to the
deletion hooks. It is even possible that the original entity to which some
Field API data was attached has been itself deleted before the field purge
operation takes place.

Field API resolves this problem by using "pseudo-entities" during purge
operations. A pseudo-entity contains only the information from the original
entity that Field API knows about: entity type, id, revision id, and
bundle. It also contains the field data for whichever field instance is
currently being purged. For example, suppose that the node type 'story' used
to contain a field called 'subtitle' but the field was deleted. If node 37
was a story with a subtitle, the pseudo-entity passed to the purge hooks
would look something like this:

@code
  $entity = stdClass Object(
    [nid] => 37,
    [vid] => 37,
    [type] => 'story',
    [subtitle] => array(
      [0] => array(
        'value' => 'subtitle text',
      ),
    ),
  );
@endcode

See @link field Field API @endlink for information about the other parts of
the Field API.
```

## Members (derived, 4)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [field_purge_batch()](../modules/field/field.crud.inc/field_purge_batch.md) (function) — Purges a batch of deleted Field API data, instances, or fields.
- [field_purge_data()](../modules/field/field.crud.inc/field_purge_data.md) (function) — Purges the field data for a single field on a single pseudo-entity.
- [field_purge_field()](../modules/field/field.crud.inc/field_purge_field.md) (function) — Purges a field record from the database.
- [field_purge_instance()](../modules/field/field.crud.inc/field_purge_instance.md) (function) — Purges a field instance record from the database.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
