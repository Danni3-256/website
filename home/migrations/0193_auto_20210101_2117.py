# Generated by Django 3.1.4 on 2021-01-01 21:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0192_auto_20201207_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcommunity',
            name='coc_committee',
            field=models.CharField(blank=True, help_text='If you do not have a formal Code of Conduct committee, please note this.', max_length=3000, verbose_name='(Optional) What are the names of all Code of Conduct committee members?'),
        ),
        migrations.AddField(
            model_name='newcommunity',
            name='demographics',
            field=models.TextField(blank=True, help_text='Most communities come to Outreachy to improve the diversity of their community. Please be honest about the demographic make up of your community', max_length=3000, verbose_name='(Optional) What is the demographics of your community?'),
        ),
        migrations.AddField(
            model_name='newcommunity',
            name='inclusive_practices',
            field=models.TextField(blank=True, help_text='Many communities come to Outreachy hoping to learn more inclusive practices. Please be honest about what steps your community has taken to become more inclusive. Please be clear on what steps you have completed vs. what you are planning to do.', max_length=3000, verbose_name='(Optional) How is your community working to become more inclusive?'),
        ),
        migrations.AddField(
            model_name='newcommunity',
            name='mentorship_programs',
            field=models.TextField(default='None', help_text='Note when your community participated in each program and how many interns the community worked with. Examples of mentoring programs include Rails Girls Summer of Code, Google Summer of Code, Google Code In, Google Season of Docs, Linux Foundation Community Bridge, and GitHub Major League Hacking internships.', max_length=3000, verbose_name='What other mentorship programs has your community participated in?'),
        ),
        migrations.AddField(
            model_name='newcommunity',
            name='participating_orgs_in_goverance',
            field=models.CharField(blank=True, help_text='If there are many organizations, list the top five organizations.', max_length=3000, verbose_name='(Optional) What different organizations and companies participate in the governance of this FOSS community?'),
        ),
        migrations.AddField(
            model_name='newcommunity',
            name='reason_for_participation',
            field=models.CharField(blank=True, max_length=3000, verbose_name='(Optional) Why does your community want to work with Outreachy?'),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(help_text="The community name you provide will be used to generate unique identifier. The identifier will be used in Outreachy website URLs to reference your community. To ensure old links remain valid, modifying the community name later will not change the community's unique identifier.", max_length=50, verbose_name='Community name'),
        ),
        migrations.AlterField(
            model_name='community',
            name='website',
            field=models.URLField(blank=True, verbose_name='(Optional) Community website URL'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='cla',
            field=models.URLField(blank=True, verbose_name='(Optional) Contributor License Agreement (CLA) URL'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='code_of_conduct',
            field=models.URLField(blank=True, verbose_name="(Optional) Community's Code of Conduct URL"),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='dco',
            field=models.URLField(blank=True, verbose_name='(Optional) Developer Certificate of Origin (DCO) agreement URL'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='governance',
            field=models.URLField(blank=True, verbose_name='(Optional) Community governance model URL'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='proprietary_software_description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='(Optional) Proprietary software details. If any internship project under your community will further the interests of proprietary software, please explain.'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='unapproved_advertising_description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='(Optional) Company advertisements on community resources. If your community resources advertise the services of only one company or organization, please explain.'),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='unapproved_license_description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='(Optional) Non-free software license details. If your FOSS community uses a license that is not an OSI-approved and FSF-approved license OR a Creative Commons license, please provide a description and links to the non-free licenses.'),
        ),
    ]
