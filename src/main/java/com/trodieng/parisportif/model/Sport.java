package com.trodieng.parisportif.model;

import javax.persistence.*;

import org.openxava.model.*;

import lombok.*;

@Entity @Getter @Setter
public class Sport extends Identifiable  {
	@Column
	private String description;

}
