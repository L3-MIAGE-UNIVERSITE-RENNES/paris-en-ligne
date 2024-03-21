package com.trodieng.parisportif.model;

import java.time.*;

import javax.persistence.*;

import org.openxava.annotations.*;
import org.openxava.model.*;

import lombok.*;
@Entity @Getter @Setter
public class evenement extends Identifiable  {
	@Column
	private String description;
	@Column
	private float cote;
	@Column
    private String score;
	@Column
    private LocalDate date;
	@ManyToOne( 
	        fetch=FetchType.LAZY,
	        optional=true)
	@DescriptionsList
	Sport sport;

}
